<?php

namespace App;

// use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Auth;

class SecretLink
{
    // Laravel is a web application framework with expressive, elegant syntax.
    //
    // PHP is ......
    //
    // 
    // hide some secrets  in source code :))
	protected static $key = 'A034C3B730054BCD';
	protected static $iv = 'C4FF5B30AF38CBBF';

    public static function generateAddLink(string $itemname, float $price) {
    	return openssl_encrypt(http_build_query(array(
    		'itemname' => $itemname,
            'price' => $price,
    		'lang' => Auth::user()->lang,
    		'time' => time()
    	)), 'AES-128-CBC', self::$key, 0, self::$iv);
    }

    public static function getUserLang() {
    	return Auth::user()->lang;
    }

    public static function decodeSecret(string $secret) {
    	$decrypted = openssl_decrypt($secret, 'AES-128-CBC', self::$key, 0, self::$iv);
        $ret = array();

        if (!$decrypted) {
            $ret['error'] = 'Invalid secret.';
        }
        else {
            parse_str($decrypted, $ret);

            if (time() > $ret['time'] + (60 * 5)) {
                $ret['error'] = 'Time limit exceeded.';
            }
        }

    	return $ret;
    }

    public static function generateDelLink(string $itemid) {
        return openssl_encrypt(http_build_query(array(
            'id' => $itemid,
            'time' => time()
        )), 'AES-128-CBC', self::$key, 0, self::$iv);
    }
}
