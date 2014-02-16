/**
 * Created by adrian on 16.02.14.
 */
$( document ).ready(function() {
    $(function() {
        $(".btn-remove").click( function(e)
            {
                e.preventDefault();
                id = $(this).attr('id');
                data =  {'id':id};
                $.post( "remove", data, function( d ) {
                    location.reload();
                });
            }
          );
    });
});
