<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Auth;

class SettingsController extends Controller
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
        return view('settings')->with('sel_lang', Auth::user()->lang);
    }

    public function save(Request $request) {
        $data = $request->validate([
            'lang' => 'required|in:en,fr'
        ]);

        DB::update('UPDATE users SET lang = ? WHERE id = ?', [$data['lang'], Auth::user()->id]);
        return view('settings')->with('is_post', true)->with('sel_lang', $data['lang']);
    }
}
