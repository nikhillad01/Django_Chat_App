app.controller('loginctrl', function ($scope,services,$state)
 {

    $scope.loginctrl = function(){
     console.log('loginctrl');
     var user = {
         email : $scope.email,
         password : $scope.password
     }
     console.log(user)
     services.loginUser(user).then(
        function success(response) {
          console.log("successful login");
          location.replace("http://127.0.0.1:8000/accounts/login")
          console.log(response);
          console.log(response.data);
          $state.go("http://127.0.0.1:8000/");
        },
        function error(response) {

          console.log("unsuccessful login");
          console.log(response);
          console.log(response.data);
  
        },
      );
    }
 })



 
