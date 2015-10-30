var myApp = angular.module("myApp",["LocalStorageModule"] );
 

myApp.controller("saveController", function($scope,$http,localStorageService) {

    //$scope.model={"text1":"text1","text2":"text2","text3":"text3"};
    
    if(!localStorageService.get("boats")){
        //localStorageService.set("model1", $scope.model1);
        console.log("boats not exists");
        $http.get("data/data.json").success(function(data) {
            $scope.boats = data;
        //console.log(data);
        });        
            console.log(localStorageService.set("boats",$scope.data));        
    }
    
    $scope.boats= localStorageService.get("boats");

    $scope.inport = 0;
    $scope.insea = 0;
    for (var i in $scope.boats) {        
        if ($scope.boats[i]["sea"]){
            $scope.insea ++;
        } else {
            $scope.inport ++;
        }
    }

    $scope.Save = function (nboats) {  
    var boats = {};
    $scope.inport = 0;
    $scope.insea = 0;
    for (i in nboats) {
            boats[i] = nboats[i];
        };      
        localStorageService.set("boats",boats); 
        for (var i in $scope.boats) {        
        if ($scope.boats[i]["sea"]){
            $scope.insea ++;
        } else {
            $scope.inport ++;
        }
        }       
      }

    $scope.RemoveAll = function (nboats) {        
        localStorageService.clearAll();
    }
    //$scope.boats_jsonstring=JSON.stringify($scope.model);
    
});