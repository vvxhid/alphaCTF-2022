<?php

use App\Lang;
use Illuminate\Support\Facades\Auth;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('home');
});

Auth::routes();

//Route::get('/home', 'HomeController@index')->name('home');
Route::get('/home', function () {
	return redirect('/');
});

Route::get('/cart', 'CartController@index')->name('cart');

Route::get('/settings', 'SettingsController@index')->name('settings');
Route::post('/settings', 'SettingsController@save');
Route::get('/cart/add', 'CartController@add')->name('cart_add');
Route::get('/cart/delete', 'CartController@delete')->name('cart_delete');