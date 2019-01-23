// // app.service('userservices', function ($http) {
// app.service('services', function ($http, $location) {
//     this.registerUser = function (user) {
//       $http({
//         method: 'GET',//issues a post request top the following url
//         url: 'http://localhost:3000/registration',
//         data: user
//       }).then(
//         function sucess(response) {
//           console.log("successful registration");
//           console.log(response);
//           console.log(response.data);
  
//         },
//         function error(response) {
  
//           console.log("unsuccessful registration");
//           console.log(response);
//           console.log(response.data);
  
//         },
//       );
//     }});


app.service('services',function ($http, $location) {

  /**
   * @description define registerUser() function to register user and passing user data as an argument
   * @param user data
   */
  this.registerUser = function(user) {
      /**
       * declaring $http variable and returning to get an instance after $http service
       * to make rest API calls
       */
     return $http({
          //declaring method type
          method: 'POST',
          //calling register API call
          url: 'http://127.0.0.1:8000/accounts/signup/',
          //sending user register data
          data: user
      })
  },
  
 this.loginUser = function (user) {
    return $http({
         //declaring method type
         method: 'POST',
         //calling register API call
         url: 'http://127.0.0.1:8000/',
         //sending user register data
         data: user
     })
 }

});