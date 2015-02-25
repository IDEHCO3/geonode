(function(){
    var app = angular.module("layer_app",[]);
    var data = {'layerName' : '',
                'layerType' : '',
                'attributes': [],
                'csrfmiddlewaretoken': ''};

    app.layerController = function($scope,$http){

        $scope.layerName = 'myLayer';
        $scope.layerType = 'Point';
        $scope.attributes = [{  'id': 0,
                                'attributeName': 'id',
                                'attributeType': 'Long',
                                'attributeSize': 10,
                                'attributeDecimal': 0 }];

        $scope.attributeName = 'name';
        $scope.attributeType = 'Character';
        $scope.attributeSize = 0;
        $scope.attributeDecimal = 0;

        this.setAttributeType = function(type){
            $scope.attributeType = type;
        };

        this.isSet = function(type){
            return $scope.attributeType === type;
        };

        this.hasSize = function(){
            if( $scope.attributeType === 'Date'){
                return false;
            }
            else{
                return true;
            }
        };

        this.hasDecimal = function(){
            if( $scope.attributeType === 'Number' ){
                return true;
            }
            else{
                return false;
            }
        };

        this.createAttribute = function(){

            if( $scope.attributeName === '' )
                return;

            if( this.hasSize() && $scope.attributeSize === 0 )
                return;

            if( this.hasDecimal() && $scope.attributeDecimal === 0 )
                return;

            $scope.attributes.push({'id': $scope.attributes.length,
                                    'attributeName': $scope.attributeName,
                                    'attributeType':  $scope.attributeType,
                                    'attributeSize': $scope.attributeSize,
                                    'attributeDecimal': $scope.attributeDecimal });

            $scope.attributeName = 'name';
            $scope.attributeType = 'Character';
            $scope.attributeSize = 0;
            $scope.attributeDecimal = 0;

            data = {'layerName' : $scope.layerName,
                    'layerType' : $scope.layerType,
                    'attributes' : $scope.attributes};

        };

        this.removeAttribute = function(index){

            $scope.attributes.splice(index,1);

            for(var i=0; i < $scope.attributes.length; i++){
                $scope.attributes[i]['id'] = i;
            }
        };

        this.editAttribute = function(index){
            $scope.attributeName = $scope.attributes[index]['attributeName'];
            $scope.attributeType = $scope.attributes[index]['attributeType'];
            $scope.attributeSize = $scope.attributes[index]['attributeSize'];
            $scope.attributeDecimal = $scope.attributes[index]['attributeDecimal'];
            this.removeAttribute(index);
        };

        this.createLayer = function(url, token){
            data = {'layerName' : $scope.layerName,
                    'layerType' : $scope.layerType,
                    'attributes': $scope.attributes };

            data = angular.toJson(data);
            data = "csrfmiddlewaretoken="+token+"& layer_data1234="+data;

            $http({
                method: 'POST',
                url: url,
                data: data,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            });

        };

    };

    app.controller("LayerController",['$scope','$http', app.layerController]);

    app.directive("attributesList", function(){
        return {
            restrict: 'E',
            templateUrl: '/static/layerEditor/attributes-list.html',
            controller: 'LayerController',
            controllerAs: 'layer'
        };
    });

    app.directive("layerInput", function(){
        return {
            restrict: 'E',
            templateUrl: '/static/layerEditor/layer-input.html',
            controller: 'LayerController',
            controllerAs: 'layer'
        };
    });

})();