(function(){
    var app = angular.module("layer_app",[]);
    var data = {'layerName' : '',
                'layerType' : '',
                'attributes': [],
                'csrfmiddlewaretoken': ''};

    data.attributes.push({   'attributeName': 'id',
                                'attributeType': 'L',
                                'attributeSize': 10,
                                'attributeDecimal': 0 });

    app.controller("FormController", function(){
        this.attributeType = 'C';

        this.setAttributeType = function(type){
            this.attributeType = type;
        };

        this.isSet = function(type){
            return this.attributeType === type;
        };

        this.hasSize = function(){
            if( this.attributeType === "D"){
                return false;
            }
            else{
                return true;
            }
        };

        this.hasDecimal = function(){
            if( this.attributeType === "N" ){
                return true;
            }
            else{
                return false;
            }
        };
    });

    app.layerController = function($http){
        this.layerName = '';
        this.layerType = '';
        this.attributes = [{   'attributeName': 'id',
                                'attributeType': 'L',
                                'attributeSize': 10,
                                'attributeDecimal': 0 }];

        this.attributeName = '';
        this.attributeType = 'C';
        this.attributeSize = '';
        this.attributeDecimal = '';

        this.createAttribute = function(){
            this.attributes.push({'attributeName': this.attributeName,
                                    'attributeType':  this.attributeType,
                                    'attributeSize': this.attributeSize,
                                    'attributeDecimal': this.attributeDecimal });

            this.attributeName = '';
            this.attributeType = 'C';
            this.attributeSize = '';
            this.attributeDecimal = '';

            data = {'layerName' : this.layerName,
                    'layerType' : this.layerType,
                    'attributes' : this.attributes};

        };

        this.createLayer = function(url, token){
            data = {'layerName' : this.layerName,
                    'layerType' : this.layerType,
                    'attributes' : this.attributes,
                    'csrfmiddlewaretoken': token};

            var response = $http.post(url,data);

            response.success(function(){

            });

            response.error(function(){

            });
        };

        this.getAttributes = function(){
            return data.attributes;
        };

    };


    app.controller("LayerController",['$http', app.layerController]);

    app.directive("attributesList", function(){
        return {
            restrict: 'E',
            templateUrl: '/static/layerEditor/attributes-list.html',
            controller: 'LayerController',
            controllerAs: 'layer'
        };
    });

})();




















//var num_atr = 1;
//$(document).ready(function(){
//    $("#add-line").click(function(){
//        var $atr_list = $("#attributes-list");
//        var $input = $("#attr_name");
//        var $attr_n = $("#attr_l");

//        num_atr++;
//        $attr_n.attr("id","attr_l"+num_atr.toString());
//        $input.attr("id","attr_name"+num_atr.toString());
//        $input.attr("name","attr_name"+num_atr.toString());

//        var $line = $("#attribute_line");
//        $atr_list.html( $atr_list.html() + $line.html() );

//        $input.attr("id","attr_name");
//        $input.removeAttr("name");
//        $attr_n.attr("id","attr_l");
//    });

//    $("#remove-line").click(function(){
//        if( num_atr > 1){
//            $("#attr_l"+num_atr.toString()).remove();
//            num_atr--;
//        }
//    });
//});