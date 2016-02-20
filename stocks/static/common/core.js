// Setup django-angular - http://django-angular.readthedocs.org/en/latest/integration.html
/**
var my_app = angular.module('OmniTrader', ['ng.django.forms']).config(function ($httpProvider, $interpolateProvider) {

    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

    //Change angular symbols to avoid collision with django. Another recommended way is to use verbatim tag.
    //$interpolateProvider.startSymbol('{$');
    //$interpolateProvider.endSymbol('$}');
});

**/