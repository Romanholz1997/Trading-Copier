$(document).ready(function() {
    $('#tableMaster').DataTable({
        "ajax": {
            "url": "/data",
            "dataSrc": ""
        },
        "columns": [
            { "data": "id" },
            { "data": "account" },
            { "data": "mode" },
            { "data": "balance" },
            { "data": "equity" },
            { "data": "margin" },
            { "data": "openTrades" },
            { "data": "plan" },
            { "data": "onOff" },
            { 
                "data": null, // Use null here since we are rendering custom HTML
                "render": function(data, type, row) {
                    // Assuming 'status' is part of the 'row' object
                    if(row.status === "success")
                    {
                        return "<span class='badge bg-success'>Active</span>"; // Render the badge based on status
                    }
                    else if(row.status === "inactive")
                    {
                        return "<span class='badge bg-secondary'>Inactive</span>"; // Render the badge based on status
                    }
                    else{
                        return "<span class='badge bg-warning'>Pending</span>"; // Render the badge based on status
                    }
                }
            }
        ],
        "lengthChange": true, // This hides the length select dropdown
        // "dom": 'frtip<"bottom"l>', // Move length change dropdown to the bottom
        //"dom": 'rt<"bottom"ilp>', // Table at the center, info and pagination at the bottom
        "dom": 'rt<"bottom"<"left"li><"right"p>>', // Position length select at bottom left
        // "dom": '<"top"lf>rt<"bottom"ip>',
        // "dom": 'rt<"bottom"ip>', // Table at the center, info and pagination at the bottom
        "searching": false, // This is true by default, but you can specify it       
        "language": {
            "paginate": {
                "first": '<<', // First page icon
                "last": '>>', // Last page icon
                "next": '>', // Next page icon
                "previous": '<' // Previous page icon
            }
        }
    });
    // $('#tableMaster_length').appendTo('.bottom').css({
    //     'float': 'left', // Ensure it stays on the left
    //     'margin-right': '20px' // Optional: Add some space to the right
    // });
});
