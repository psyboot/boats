var myApp = angular.module('myApp', []);

myApp.controller('todoCtrl', function ($scope,$http) {
    $scope.test = "Yep";
    $scope.todos = [
        {name:"Вася", last:"Иванов", boat:"123", sea:false},
        {name:"Петя", last:"Сидоров", boat:"345", sea:false}
    ];
    $http.get("data/data.json").success(function(data) {
        $scope.boats = data;
    });
    $scope.Save = function (nboats) {
        console.log(nboats);
        $http.post("data/data.json", nboats).success(function(data) {console.log(data);});
    }
    console.log($scope.todos);
});