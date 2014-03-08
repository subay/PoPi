$( document ).ready(function() {
    $(function() {
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
            var dcArray = [ 'dc10', 'dc20', 'dc30', 'dc40', 'dc50']
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
            $.each( dcArray, function( intValue, currentElement ) {
                $('.btn-edit').getChecked(btnid, currentElement);
            });
            var id = ($(updateObject).get(0));
            var name = ($(updateObject).get(1));
            var hc = ($(updateObject).get(2))+($(updateObject).get(3)+($(updateObject).get(4))+($(updateObject).get(5))+($(updateObject).get(6)));
            var dc = ($(updateObject).get(7))+($(updateObject).get(8)+($(updateObject).get(9))+($(updateObject).get(10))+($(updateObject).get(11)));
            var data =  {'id':id,'name':name, 'hc':hc,'dc':dc};
            //console.log(data);
            $.post( "edit", data, function( d ) {
                location.reload();
            });
        });
    });
});


