$('th.Sortable').click(function(){

    var form = $('#formfilters')

    if($(this).hasClass('Nome')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("nome")
            form.find("#id_direction").val("desc")
            //url = appendTo_url("order_by=nome&direction=desc", url)
        }else{
            form.find("#id_order_by").val("nome")
            form.find("#id_direction").val("asc")    
        }
    }else if($(this).hasClass('Tipo')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("tipoTarefa")
            form.find("#id_direction").val("desc")
            //url = appendTo_url("order_by=tipoTarefa&direction=desc", url)
        }else{
            form.find("#id_order_by").val("tipoTarefa")
            form.find("#id_direction").val("asc")
            //url = appendTo_url("order_by=tipoTarefa&direction=asc", url)
        }
    }else if($(this).hasClass('Estado')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("estado")
            form.find("#id_direction").val("desc")
            //url = appendTo_url("order_by=estado&direction=desc", url)
        }else{
            form.find("#id_order_by").val("estado")
            form.find("#id_direction").val("asc")
            //url = appendTo_url("order_by=estado&direction=asc", url)
        }
    }
    form.submit()
})  

$(document).ready( function(){
    $('th.Sortable').each(function(){
        $(this).has('i').addClass('tableBorder')
    })
})


$('.delete').click(function (){
    var data_var = $(this).data('id');
    $("#deleteModal").attr("action", data_var);
})


$(".expand").hide();

$("table").click(function(event) {
    //event.stopPropagation();
    var target = $(event.target);
    if(!target.is('a') && !target.is('button')){
        if ( target.closest('tbody').find('i').hasClass('fas fa-chevron-right') ){
            target.closest('tbody').next().show();
            target.closest('tbody').find('i').removeClass();
            target.closest('tbody').find('i').addClass('fas fa-chevron-down');	

        }else if( target.closest('tbody').find('i').hasClass('fas fa-chevron-down') ){
            target.closest('tbody').next().hide();
            target.closest('tbody').find('i').removeClass();
            target.closest('tbody').find('i').addClass('fas fa-chevron-right');	

        }    				
    }
})