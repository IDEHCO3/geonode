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
                                'attributeType': 'Number',
                                'attributeSize': 10,
                                'attributeDecimal': 0 }];

        $scope.attributeName = 'attributeName';
        $scope.attributeType = 'Character';
        $scope.attributeSize = 50;
        $scope.attributeDecimal = 0;

        this.setAttributeType = function(type){
            $scope.attributeType = type;
        };

        this.isSet = function(type){
            return $scope.attributeType === type;
        };

        this.hasSize = function(){
            if( $scope.attributeType === 'Date' || $scope.attributeType === 'Logical'){
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

            if( $scope.attributeType === 'Date'){
                $scope.attributeSize = 8;
            }
            else if( $scope.attributeType === 'Logical' ){
                $scope.attributeSize = 1;
            }

            if( typeof $scope.attributeSize != 'number' )
                return;

            if( typeof $scope.attributeDecimal != 'number' )
                return;

            if( $scope.attributeSize > 255 || $scope.attributeSize <= 0 )
                return;

            if( $scope.attributeDecimal > 255 || $scope.attributeDecimal < 0 )
                return;

            $scope.attributes.push({'id': $scope.attributes.length,
                                    'attributeName': $scope.attributeName,
                                    'attributeType':  $scope.attributeType,
                                    'attributeSize': $scope.attributeSize,
                                    'attributeDecimal': $scope.attributeDecimal });

            $scope.attributeName = 'attributeName';
            $scope.attributeType = 'Character';
            $scope.attributeSize = 50;
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