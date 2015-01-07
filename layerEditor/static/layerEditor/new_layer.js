var num_atr = 0;
$(document).ready(function(){
    $("#add-line").click(function(){
        var $atr_list = $("#attributes-list");
        var $input = $("#attr_name");
        var $attr_n = $("#attr_l");

        num_atr++;
        $attr_n.attr("id","attr_l"+num_atr.toString());
        $input.attr("id","attr_name"+num_atr.toString());
        $input.attr("name","attr_name"+num_atr.toString());

        var $line = $("#attribute_line");
        $atr_list.html( $atr_list.html() + $line.html() );

        $input.attr("id","attr_name");
        $input.removeAttr("name");
        $attr_n.attr("id","attr_l");
    });

    $("#remove-line").click(function(){
        if( num_atr != 0){
            $("#attr_l"+num_atr.toString()).remove();
            num_atr--;
        }
    });
});