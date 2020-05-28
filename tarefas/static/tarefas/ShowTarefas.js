$('th.Sortable').click(function(){
    if($(this).hasClass('Nome')){
        if($(this).hasClass('asc'))
            window.location.href =  "?order_by=nome&direction=desc"
        else
            window.location.href =  "?order_by=nome&direction=asc"
    }
})  