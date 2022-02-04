@extends('layouts.app')
@php($lang = \App\Lang::getLang(Auth::user()->lang))
@section('content')
<div class="container" style="padding-top: 20px; padding-bottom: 20px;">
    <div class="row">
        <h1 style="color: white">{{ $lang['your_cart'] }}</h1>
    </div>
    <div class="row">
		<ul class="list-group" style="width: 100%">
			@php($total = 0)
			@foreach ($items as $item)
				<li class="list-group-item list-group-item-action list-group-item-dark">
					<div class="row">
						<div class="col-8">{{ $item->name }}</div>
						<div class="col-4 text-right">
							{{ number_format($item->price, 2) }}
							<button type="button" class="btn btn-danger" style="margin-left: 10px" data-itemid="{{ $item->id }}"><i class="fas fa-trash-alt"></i></button>
						</div>
					</div>
				</li>
				@php($total += $item->price)
			@endforeach

			<li class="list-group-item list-group-item-action list-group-item-dark active">
				<div class="row">
					<div class="col-8"><b>{{ $lang['total'] }}</b></div>
					<div class="col-4 text-right"><b style="margin-right: 55px">{{ number_format($total, 2) }}</b></div>
				</div>
			</li>
		</ul>
    </div>
    <div class="row" style="margin-top: 20px">
    	<div class="col text-right">
    		<button class="btn btn-primary"><i class="fas fa-money-bill-wave"></i> {{ $lang['checkout'] }}</a></button>
    	</div>
    </div>
</div>
<script>
	setTimeout(function(){window.location.reload()}, 1000 * 60 * 5);
	$(function () {
		$('.fa-money-bill-wave').parent().click(function () {
			alert('{{ $lang['overdemand'] }}');
		});
		$('.fa-trash-alt').parent().click(function () {
			var secret,
                btn = $(this);

            switch (btn.data('itemid')) {
            	@foreach ($items as $item)
	                case {{ $item->id }}: secret = '{{ \App\SecretLink::generateDelLink($item->id) }}'; break;
                @endforeach
            }
            btn.addClass('disabled');
            $.get('{{ route('cart_delete') }}', {
                secret: secret,
                _token: '{{ csrf_token() }}'
            }).done(function (resp) {
                btn.removeClass('disabled');
                alert(resp);
                window.location.reload();
            });
		});
	});
</script>
@endsection