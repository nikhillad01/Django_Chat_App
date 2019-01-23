// var app = angular.module('app', ['ui.router']);
var app = angular.module('mainapp', ['ui.router'], function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  });

app.config(['$stateProvider','$urlRouterProvider',function($stateProvider,$urlRouterProvider) {
    $stateProvider
    // .state('login',{
    //     url:'/login', //hashed url(user goes to this url)
    //     templateUrl:'Templates/login.html',//binds the content from this html
    //     controller:'loginctrl' //goes to controller and binds it with a scope
    // })
    .state( 'registration',{
        url:'/registration',
        templateUrl:'Templates/registrationform.html',
        //controller:'registrationctrl'
        controller:'registration'
       
    })
    .state( 'login',{
        url:'/login', //hashed url(user goes to this url)
        templateUrl:'Templates/login.html',//binds the content from this html
        controller:'loginctrl' //goes to controller and binds it with a scope
    })
    .state(  'dashboard',{
        url:'/dashboard',
        templateUrl:'Templates/dashboard.html'

    })

    $urlRouterProvider.otherwise('login');

}]);

