<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\SecretLink;
use App\Lang;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Auth;

class CartController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $items = DB::select('SELECT * FROM cart WHERE user_id = ?', [Auth::user()->id]);

        return view('cart')->with('items', $items);
    }

    public function add(Request $request) {
        $data = $request->validate([
            'secret' => 'required',
            '_token' => 'required'
        ]);

        if($data['_token'] !== csrf_token()) {
            return 'Invalid token.';
        }

        $data = SecretLink::decodeSecret($data['secret']);

        if (isset($data['error'])) {
            return $data['error'];
        }

        DB::insert('INSERT INTO cart (user_id, name, price) VALUES (?, ?, ?)', [Auth::user()->id, Lang::getLang($data['lang'])[$data['itemname']], $data['price']]);

        return 'Item added to cart successfuly.';
    }

    public function delete(Request $request) {
        $data = $request->validate([
            'secret' => 'required',
            '_token' => 'required'
        ]);

        if($data['_token'] !== csrf_token()) {
            return 'Invalid token.';
        }

        $data = SecretLink::decodeSecret($data['secret']);

        if (isset($data['error'])) {
            return $data['error'];
        }

        $user = DB::table('cart')->where('id', $data['id'])->first();

        if (!$user) {
            return 'Invalid id.';
        }
        else {
            if ($user->user_id !== Auth::user()->id) {
                return 'You are not allowed to remove cart items of another user.';
            }
            else {
                DB::delete('DELETE FROM cart WHERE id = ?', [$data['id']]);
                return 'Item removed from cart successfully.';
            }
        }
    }
}
