$( document ).ready(function() {
    $(function() {
        $(".btn-on").click( function(e)
            {
                e.preventDefault();
                var id = $(this).attr('id');
                console.log('on '+id);
                data = {'id':id,'status':'1'};
                $.post( "/", data, function( d ) {
                    location.reload();
                });
            }
        );
        $(".btn-off").click( function(e)
            {
                e.preventDefault();
                var id = $(this).attr('id');
                console.log('on '+id);
                data = {'id':id,'status':'0'};
                $.post( "/", data, function( d ) {
                    location.reload();
                });
            }
        );
        $(".btn-remove").click( function(e)
            {
                e.preventDefault();
                var id = $(this).attr('id');
                var data =  {'id':id};
                $.post( "remove", data, function( d ) {
                    location.reload();
                });
            }
        );
        $(".btn-edit").click( function(e) {
            e.preventDefault();
            var hcArray = [ 'hc10', 'hc20', 'hc30', 'hc40', 'hc50']
            var btnid = $(this).attr('id');
            var updateObject = [$(this).attr('id') ,$('#name'+btnid).val()];
            $.fn.getChecked = function (id,xc) {
                if($('#'+xc+id).is(':checked')) {
                    updateObject.push('0');
                } else {
                    updateObject.push('1');
                }
            };
            $.each( hcArray, function( intValue, currentElement ) {
                $('.btn-edit').getChecked(btnid, currentElement);
            });
            var id = ($(updateObject).get(0));
            var name = ($(updateObject).get(1));
            var hc = ($(updateObject).get(2))+($(updateObject).get(3)+($(updateObject).get(4))+($(updateObject).get(5))+($(updateObject).get(6)));
            var dc = $('input[name="dc"]:checked').val();
            var data =  {'id':id,'name':name,'hc':hc,'dc':dc};
            //console.log(data);
            $.post( "edit", data, function( d ) {
                location.reload();
            });
        });
    });
});


