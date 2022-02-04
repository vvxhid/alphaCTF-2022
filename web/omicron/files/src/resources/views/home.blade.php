@extends('layouts.app')

@php($lang = \App\Lang::getLang(Auth::user() ? Auth::user()->lang : 'en'))

@section('content')
<style>
    .card {
        margin: 0 auto;
    }

    .card-body {
        height: 250px;
    }
</style>
<script>
    setTimeout(function(){window.location.reload()}, 1000 * 60 * 5);

    $(function () {
        $('.fa-cart-plus').parent().click(function () {
            @guest

                alert('{{ $lang['have_to_log_in'] }}');

            @else

                var secret,
                    btn = $(this);

                switch (btn.data('itemid')) {
                    case 0: secret = '{{ \App\SecretLink::generateAddLink('toilet_paper', 13.37) }}'; break;
                    case 1: secret = '{{ \App\SecretLink::generateAddLink('hand_sanitizer', 133.7) }}'; break;
                    case 2: secret = '{{ \App\SecretLink::generateAddLink('surgical_masks', 1337.00) }}'; break;
                }

                btn.addClass('disabled');

                $.get('{{ route('cart_add') }}', {
                    secret: secret,
                    _token: '{{ csrf_token() }}'
                }).done(function (resp) {
                    btn.removeClass('disabled');
                    alert(resp);
                });

            @endguest
        });
    });
</script>

<div class="container" style="padding-top: 20px">
    <div class="row">
        <div class="col-sm">
            <div class="card text-white bg-dark border-light mb-3" style="width: 18rem;">
                <img src="{{ asset('/img/toiletpaper.jpg') }}" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">{{ $lang['toilet_paper'] }}</h5>
                    <p class="card-text">
                        <p style="text-align: justify;">{{ $lang['toilet_paper_desc'] }}</p>
                        <p>{{ $lang['price'] }}: 13.37</p>
                    </p>
                </div>
                <div class="card-footer text-right">
                    <a href="#" class="btn btn-primary" data-itemid="0"><i class="fas fa-cart-plus"></i> {{ $lang['add_to_cart'] }}</a>
                </div>
            </div>
        </div>

        <div class="col-sm">
            <div class="card text-white bg-dark border-light mb-3" style="width: 18rem;">
                <img src="{{ asset('/img/handsanitizer.webp') }}" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">{{ $lang['hand_sanitizer'] }}</h5>
                    <p class="card-text">
                        <p style="text-align: justify;">{{ $lang['hand_sanitizer_desc'] }}</p>
                        <p>{{ $lang['price'] }}: 133.7</p>
                    </p>
                </div>
                <div class="card-footer text-right">
                    <a href="#" class="btn btn-primary" data-itemid="1"><i class="fas fa-cart-plus"></i> {{ $lang['add_to_cart'] }}</a>
                </div>
            </div>
        </div>

        <div class="col-sm">
            <div class="card text-white bg-dark border-light mb-3" style="width: 18rem;">
                <img src="{{ asset('/img/surgicalmask.jpg') }}" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">{{ $lang['surgical_masks'] }}</h5>
                    <p class="card-text">
                        <p style="text-align: justify;">Allan please add details</p>
                        <p>{{ $lang['price'] }}: 1337.00</p>
                    </p>
                </div>
                <div class="card-footer text-right">
                    <a href="#" class="btn btn-primary" data-itemid="2"><i class="fas fa-cart-plus"></i> {{ $lang['add_to_cart'] }}</a>
                </div>
            </div>
        </div>
    </div>
</div>
<footer>
    <div class="row bg-dark">
        <div class="col">
            <p style="color: gray; margin-top: 10px; margin-left: 10px;">* {{ $lang['illustration_only'] }}</p>
        </div>
    </div>
</footer>
@endsection