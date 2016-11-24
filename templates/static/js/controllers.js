mainApp.controller('MainCtrl', ['$scope','$http', function($scope, $http) {

// form json object for posting data
$scope.date = new Date();
$scope.genderList = [
  {type:'male'},
  {type:'female'}
];
$scope.patient = {};
$scope.patient.gender = $scope.genderList[0].type;
// end of json object 
    
// Pagination part start
$scope.currentPage = 1;
$scope.numPerPage = 5;
$scope.paginate = function (value) {  
    var begin, end, index;  
    begin = ($scope.currentPage - 1) * $scope.numPerPage;  
    end = begin + $scope.numPerPage;  
    index = $scope.patientLits.indexOf(value);
    return (begin <= index && index < end);  
};
// end of pagination 

// form validation part
$scope.getAge = function(value){
  var date = new Date(value);
  var ageDifMs = Date.now() - date.getTime();
  var ageDate = new Date(ageDifMs);
  $scope.patient.age = Math.abs(ageDate.getUTCFullYear() - 1970);
}      
// end of validation part ..

// function to submit the form after all validation has occurred            
$scope.submitForm = function(isValid) {
// check to make sure the form is completely valid
	if (isValid) {
		$scope.patient.gender = $scope.patient.gender.type
  		console.log($scope.patient);
  		$scope.AddPatient($scope.patient);
  		$(function () {
        	$('#entryform').modal('toggle');
      	});
	}
};

// ADD Patient Record to Database
$scope.AddPatient = function(patient){
	var config = {
        headers : {
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
        }
    }
    $http({
    	method:'GET',
    	url: '/addpatient/',
    	params: patient,
    	config: config
    })
	.success(function (data, status, headers, config) {
        $scope.responseData = data;
        $scope.patient = {};
        $scope.patient.age = 0;
        $scope.displyPatient();
    })
};

// get all record of patient from database
$scope.displyPatient = function(){
      $http({
      	method : "GET",
      	url : "/showpatient"
  	}).then(function (response) {
      	$scope.patientLits = response.data;
      	$scope.totalItems = $scope.patientLits.length;
  	}, function (response) {
      	$scope.patientLits = response.statusText;
  	});
};

// Delete record from database
$scope.removeItem = function(pk){
	$http({
      	method : "GET",
      	url : "/deletepatient",
      	params:{
      		'pk':pk
      	}
  	}).then(function (response) {
      	$scope.patientLits = response.data;
      	$scope.totalItems = $scope.patientLits.length;
  	}, function (response) {
      	$scope.patientLits = response.statusText;
  	});	
};

}]);
