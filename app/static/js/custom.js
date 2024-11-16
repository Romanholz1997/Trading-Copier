$(document).ready(function() {  

    var masterOpenTable = $('#tblMasterOpen').DataTable({
        "ajax": {
            "url": "/get_masterOpen",
            "dataSrc": ""
        },
        "columns": [
            { "data": "id" },
            { "data": "ticket" },
            { "data": "symbol" },
            { "data": "volume" },
            { "data": "profit" },
            { "data": "price_open" },
            { "data": "price_current" },
            { 
                "data": null, // Use null here since we are rendering custom HTML
                "render": function(data, type, row) {
                    // Assuming 'status' is part of the 'row' object
                    if(row.type === 0)
                    {
                        return "<span class='badge bg-success'>Buy</span>"; // Render the badge based on status
                    }
                    else{
                        return "<span class='badge bg-warning'>Sell</span>"; // Render the badge based on status
                    }
                }
            },
            { "data": "timestamp" },
            { "data": "flag" }            
        ],
        "lengthChange": true, // This hides the length select dropdown
        "dom": 'rt<"bottom"<"left"li><"right"p>>', // Position length select at bottom left
        "searching": false, // This is true by default, but you can specify it       
        "language": {
            "paginate": {
                "first": '<<', // First page icon
                "last": '>>', // Last page icon
                "next": '>', // Next page icon
                "previous": '<' // Previous page icon
            }
        },
        "initComplete": function(settings, json) {
            // This runs after the table has been fully initialized
            $('#masterOpen').removeClass('active');
        }
    });
    function reloadMasterOpenOrder() {
        if (masterOpenTable) {
            masterOpenTable.ajax.reload(null, false); // Reload without resetting pagination
        }
    }
    setInterval(reloadMasterOpenOrder, 3000);

    var masterCloseTable = $('#tblMasterClose').DataTable({
        "ajax": {
            "url": "/get_masterClose",
            "dataSrc": ""
        },
        "columns": [
            { "data": "id" },
            { "data": "ticket" },
            { "data": "open_ticket" },
            { "data": "symbol" },
            { "data": "volume" },
            { "data": "price_open" },
            { "data": "price_close" },
            { "data": "profit" },           
            { 
                "data": null, // Use null here since we are rendering custom HTML
                "render": function(data, type, row) {
                    // Assuming 'status' is part of the 'row' object
                    if(row.type === 0)
                    {
                        return "<span class='badge bg-success'>Buy</span>"; // Render the badge based on status
                    }
                    else{
                        return "<span class='badge bg-warning'>Sell</span>"; // Render the badge based on status
                    }
                }
            },
            { "data": "time" },
            { "data": "flag" }            
        ],
        "lengthChange": true, // Shows the length select dropdown
        "dom": 'rt<"bottom"<"left"li><"right"p>>', // Position length select at bottom left
        "searching": false, // Disable searching if not needed
        "language": {
            "paginate": {
                "first": '<<', // First page icon
                "last": '>>', // Last page icon
                "next": '>', // Next page icon
                "previous": '<' // Previous page icon
            }
        },
        "initComplete": function(settings, json) {
            // This runs after the table has been fully initialized
            $('#masterClose').removeClass('active');
        }
    });
    function reloadMasterCloseOrder() {
        if (masterCloseTable) {
            masterCloseTable.ajax.reload(null, false); // Reload without resetting pagination
        }
    }
    setInterval(reloadMasterCloseOrder, 3000);

    var slaveOpenTable = $('#tblSlaveOpen').DataTable({
        "ajax": {
            "url": "/get_slaveOpen",
            "dataSrc": ""
        },        
        "columns": [
            { "data": "id" },
            { "data": "account" },
            { "data": "ticket" },
            { "data": "open_ticket" },
            { "data": "symbol" },            
            { "data": "volume" },
            { "data": "price_open" },
            { "data": "sl" },
            { "data": "tp" },
            { 
                "data": null, // Use null here since we are rendering custom HTML
                "render": function(data, type, row) {
                    // Assuming 'status' is part of the 'row' object
                    if(row.type === 0)
                    {
                        return "<span class='badge bg-success'>Buy</span>"; // Render the badge based on status
                    }
                    else{
                        return "<span class='badge bg-warning'>Sell</span>"; // Render the badge based on status
                    }
                }
            },
            { "data": "time" },
            { "data": "flag" },          
        ],
        "lengthChange": true, // This hides the length select dropdown
        "dom": 'rt<"bottom"<"left"li><"right"p>>', // Position length select at bottom left
        "searching": false, // This is true by default, but you can specify it       
        "language": {
            "paginate": {
                "first": '<<', // First page icon
                "last": '>>', // Last page icon
                "next": '>', // Next page icon
                "previous": '<' // Previous page icon
            }
        },
        "initComplete": function(settings, json) {
            // This runs after the table has been fully initialized
            $('#solveOpen').removeClass('active');
        }
    });
    function reloadSlaveOpenOrder() {
        if (slaveOpenTable) {
            slaveOpenTable.ajax.reload(null, false); // Reload without resetting pagination
        }
    }
    setInterval(reloadSlaveOpenOrder, 3000);

    var slaveCloseTable = $('#tblSlaveClose').DataTable({
        "ajax": {
            "url": "/get_slaveClose",
            "dataSrc": ""
        },        
        "columns": [
            { "data": "id" },
            { "data": "account" },
            { "data": "ticket" },
            { "data": "open_ticket" },
            { "data": "symbol" },            
            { "data": "volume" },
            { "data": "price_close" },
            { 
                "data": null, // Use null here since we are rendering custom HTML
                "render": function(data, type, row) {
                    // Render the badge based on the 'type' property
                    return row.type === 0 
                        ? "<span class='badge bg-success'>Buy</span>" 
                        : "<span class='badge bg-warning'>Sell</span>";
                }
            },
            { "data": "time" },
            { "data": "flag" },          
        ],
        "lengthChange": true, // Show the length select dropdown
        "dom": 'rt<"bottom"<"left"li><"right"p>>', // Position length select at bottom left
        "searching": false, // Disable searching
        "language": {
            "paginate": {
                "first": '<<', // First page icon
                "last": '>>', // Last page icon
                "next": '>', // Next page icon
                "previous": '<' // Previous page icon
            }
        },
        "initComplete": function(settings, json) {
            // This runs after the table has been fully initialized
            $('#solveClose').removeClass('active');
        }
    });
    function reloadSlaveCloseOrder() {
        if (slaveCloseTable) {
            slaveCloseTable.ajax.reload(null, false); // Reload without resetting pagination
        }
    }
    setInterval(reloadSlaveCloseOrder, 3000);

    var tbl_masterAccount = $('#tblMasterAccount').DataTable({
        "ajax": {
            "url": "/get_master",
            "dataSrc": ""
        },
        "columns": [
            { "data": "id" },
            { "data": "type" },
            { "data": "account" },
            { "data": "server" },
            { "data": "plan" },
            { 
                "data": null, // Use null here since we are rendering custom HTML
                "render": function(data, type, row) {
                    // Assuming 'status' is part of the 'row' object
                    if(row.flag === 0)
                    {
                        return "<span class='badge bg-success'>Active</span>"; // Render the badge based on status
                    }
                    else{
                        return "<span class='badge bg-warning'>Pending</span>"; // Render the badge based on status
                    }
                }
            },
            { 
                "data": null,
                "orderable": false,
                "searchable": false,
                "render": function(data, type, row) {
                    return `
                        <button class="btn btn-sm btn-danger btn-delete" data-id="${row.id}">
                            <i class="fas fa-trash-alt"></i> Delete
                        </button>
                    `;
                }
            }
        ],
        "lengthChange": true, // This hides the length select dropdown
        "dom": 'rt<"bottom"<"left"li><"right"p>>', // Position length select at bottom left
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

    var tbl_slaveAccount = $('#tblSlaveAccount').DataTable({
        "ajax": {
            "url": "/get_slave",
            "dataSrc": ""
        },
        "columns": [
            { "data": "id" },
            { "data": "type" },
            { "data": "account" },
            { "data": "server" },
            { "data": "plan" },
            { 
                "data": null, // Use null here since we are rendering custom HTML
                "render": function(data, type, row) {
                    // Assuming 'status' is part of the 'row' object
                    if(row.flag === 0)
                    {
                        return "<span class='badge bg-success'>Active</span>"; // Render the badge based on status
                    }
                    else{
                        return "<span class='badge bg-warning'>Pending</span>"; // Render the badge based on status
                    }
                }
            },
            { 
                "data": null,
                "orderable": false,
                "searchable": false,
                "render": function(data, type, row) {
                    return `
                        <button class="btn btn-sm btn-danger btn-delete" data-id="${row.id}">
                            <i class="fas fa-trash-alt"></i> Delete
                        </button>
                    `;
                }
            }

        ],
        "lengthChange": true, // This hides the length select dropdown
        "dom": 'rt<"bottom"<"left"li><"right"p>>', // Position length select at bottom left
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

    $('#addMasterForm').on('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        var form = $(this); // Define the 'form' variable as a jQuery object
        $.ajax({
            type: 'POST',
            url: '/add_master',
            data: $(this).serialize(), // Serialize form data
            success: function(response) {
                // Handle success (e.g., show a message or close the modal)
                console.log(response);
                tbl_masterAccount.ajax.reload();
                $('#AddMaster').modal('hide'); // Hide modal after successful submission
                form.trigger("reset"); // Reset the form
                form.find('select').val(''); // Clear select fields
            },
            error: function(error) {
                // Handle error
                console.error(error);
            }
        });
    });

    $('#addSlaveForm').on('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        var form = $(this); // Define the 'form' variable as a jQuery object
        $.ajax({
            type: 'POST',
            url: '/add_slave',
            data: form.serialize(), // Serialize form data
            success: function(response) {
                // Handle success (e.g., show a message or close the modal)
                console.log(response);
                tbl_slaveAccount.ajax.reload();
                $('#AddSlave').modal('hide'); // Hide modal after successful submission
                form.trigger("reset"); // Reset the form
                form.find('select').val(''); // Clear select fields
            },
            error: function(error) {
                // Handle error
                console.error(error);
            }
        });
    });

    $('#tblSlaveAccount tbody').on('click', '.btn-delete', function() {
        var id = $(this).data('id');
        if (confirm('Are you sure you want to delete this record?')) {
            $.ajax({
                url: '/delete_slaveAccount',
                method: 'POST',
                data: { id: id },
                success: function(response) {
                    if(response.message){
                        alert('Record deleted successfully.');
                        tbl_slaveAccount.ajax.reload();
                    } else {
                        alert('Failed to delete the record.');
                    }
                },
                error: function(xhr, status, error) {
                    alert('An error occurred while deleting the record.');
                }
            });
        }
    });

    $('#tblMasterAccount tbody').on('click', '.btn-delete', function() {
        var id = $(this).data('id');
        if (confirm('Are you sure you want to delete this record?')) {
            $.ajax({
                url: '/delete_masterAccount',
                method: 'POST',
                data: { id: id },
                success: function(response) {
                    if(response.message){
                        alert('Record deleted successfully.');
                        tbl_masterAccount.ajax.reload();
                    } else {
                        alert('Failed to delete the record.');
                    }
                },
                error: function(xhr, status, error) {
                    alert('An error occurred while deleting the record.');
                }
            });
        }
    });
});

