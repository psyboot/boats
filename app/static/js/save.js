var myApp = angular.module('myApp', []);

myApp.controller("saveController", function($scope,$http) {
    $http.get("/boatssql",{header : {'Content-Type' : 'application/json; charset=UTF-8'}}).success(function(data)
        {
            $scope.boats = data["boats"];
                $scope.notinsea = data["seaornot"]["notinsea"];
                $scope.insea = data["seaornot"]["insea"];;
            console.log(data);
        }
        )


    $scope.Save = function (nboats) {
    var boats = {}
    // data = nboats
    $http.post("/boatssave", nboats, {header : {'Content-Type' : 'application/json; charset=UTF-8'}})
        .success(function(nboats)
        {
            console.log("Data send:");
        })
        .error(function(nboats)
        {
            console.log('error' + nboats);
        });
    $scope.notinsea = 0;
    $scope.insea = 0;
    for (i in nboats) {
            boats[i] = nboats[i];
        };

        for (var i in $scope.boats) {
        if ($scope.boats[i]["sea"]){
            $scope.insea ++;
        } else {
            $scope.notinsea ++;
        }
        }
      }

});
