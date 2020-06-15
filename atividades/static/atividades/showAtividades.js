$('.delete').click(function (){
    var data_var = $(this).data('id');
    $("#deleteModal").attr("action", data_var);
})

$('.recuse').click(function (){
    var data_var = $(this).data('id');
    $("#recuseModal").attr("action", data_var);
    console.log($(this).data('id'));
})

$('#id_localcampus').change(function(){
    $('select[name=localedicifio]').find('option').each(function(){
        $(this).remove();
    })

    campusid = $(this).val();
    request_url = '/GestaoAtividades/getEdificio/' + campusid;
    $.ajax({
        url: request_url,
        dataType: "json",
        success: function(data){
            $('select[name=localedicifio]').append(
                $('<option></option>').html("Pesquisar por Edifício").attr('disabled', 'disabled').attr('selected', 'selected')
            )
            $.each(data, function(index, text){
                $('select[name=localedicifio]').append(
                    $('<option></option>').val(index).html(text)
                )
            })
        },
    });
})

/*$(".clickable-row").on('click', function(event) {
event.stopPropagation();
var target = $(event.target);
if(!target.is('a'))
    window.location = $(this).data("href");
});*/

$(".hide").hide();

$("table").click(function(event) {
    var target = $(event.target);
    if(!target.is('a')){
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
