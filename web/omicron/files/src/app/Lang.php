<?php

namespace App;

class Lang
{
	public static function getLang(string $lang) {
        chdir(base_path() . '/resources/lang/');
        $ret = include $lang . '.php';
        return $ret;
    }
}
