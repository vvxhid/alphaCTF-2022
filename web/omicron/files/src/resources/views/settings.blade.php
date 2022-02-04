@extends('layouts.app')

@php($lang = \App\Lang::getLang($sel_lang))

@section('content')
<div class="container" style="padding-top: 20px;">
    <div class="row">
        <h1 style="color: white">{{ $lang['settings'] }}</h1>
    </div>

    @if(isset($is_post))
	    <div class="row" style="padding-top: 10px">
	    	<div class="alert alert-success" role="alert" style="width: 100%">
				{{ $lang['settings_saved'] }}
			</div>
		</div>
	@endif

	<form action="{{ route('settings') }}" method="POST">
		<div class="row" style="padding-top: 10px">
			<div class="col-4" style="color: white">
				<label for="language">{{ $lang['language'] }}</label>
			</div>
			<div class="col-8">
				{{ csrf_field() }}
				<select style="width: 100%" class="form-control" id="language" name="lang">
					<option value="en" {{ $sel_lang === 'en' ? 'selected' : '' }}>{{ $lang['english'] }}</option>
					<option value="fr" {{ $sel_lang === 'fr' ? 'selected' : '' }}>{{ $lang['french'] }}</option>
				</select>
			</div>
		</div>

		<div class="row" style="padding-top: 30px">
			<button class="btn btn-primary">{{ $lang['save'] }}</button>
		</div>
	</form>

</div>
@endsection