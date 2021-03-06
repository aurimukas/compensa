/**
 * Created by aurimas on 30/11/14.
 */
(function($) {

    "use strict";

    /**
     * Render Code column values as links to details page.
     */
    var render_code_link = function(data, type, row) {
        console.log(row);

        return data;
    };

    $(function() {
        $('#requests-list').dataTable({
            "bPaginate": true,
            //"sPaginationType": "bootstrap",
            "bScrollCollapse": true,
            //"bProcessing": true,
            "processing": true,
            //"bServerSide": true,
            "serverSide": true,
            'order': [[2, 'desc']],
            'pageLength': 30,
            //"sAjaxSource": Django.url('com_local:request_list')
            "ajax": {
                //"url": Django.url('com_local:request_list'),
                "url": "/compensa/request/list/",
                "type": "GET"
            }
        });
    });

}(jQuery));
