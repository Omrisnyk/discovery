
var LayoutManager = {
    initializers: {},

    init: function() {
        EventManager.subscribe('dataLoaded', LayoutManager.render);

        for(var handler in LayoutManager.initializers){
            LayoutManager.initializers[handler].call(this);
        }
    },

    route: function(data) {
    },

    render: function(results) {
    },

    isHomePage: function() {
        var pathArray =  window.location.pathname.split('/').join('').split('');

        if (pathArray.length == 0) {
            return true;
        }
        else {
            return false;
        }
    },

    isPoolPage: function() {
        var pathArray =  window.location.pathname.split('/');

        if ($.inArray('results', pathArray) !== -1) {
            return true;
        }
        else {
            return false;
        }
    },

    isVendorPage: function() {
        var pathArray =  window.location.pathname.split('/');

        if ($.inArray('vendor', pathArray) !== -1) {
            return true;
        }
        else {
            return false;
        }
    },

    enableVehicles: function() {
        $("div#vehicle_select select").attr("disabled", false);
    },

    disableVehicles: function() {
        $("div#vehicle_select select").attr("disabled", true);
    },

    enablePools: function() {
        $("div#pool_select select").attr("disabled", false);
    },

    showPools: function() {
        if ($("div#zone_select").is(":visible")) {
            $("#pool-id").select2({width: '200px'});
            $("#zone-id").select2({width: '200px'});
        }
        else {
            $("#pool-id").select2({width: '415px'});
        }
        $("div#pool_select").show();
    },

    disablePools: function() {
        $("div#pool_select select").attr("disabled", true);
    },

    hidePools: function() {
        $("div#pool_select").hide();

        if ($("div#zone_select").is(":visible")) {
            $("#zone-id").select2({width: '415px'});
        }
    },

    zoneActive: function() {
        var vehicle = DataManager.getVehicle();

        if (vehicle && vehicle.match(/^BMO/i)) {
            return true;
        }
        else {
            return false;
        }
    },

    enableZones: function() {
        if (LayoutManager.zoneActive()) {
            $("div#zone_select select").attr("disabled", false);
        }
    },

    showZones: function() {
        if ($("div#pool_select").is(":visible")) {
            $("#zone-id").select2({width: '200px'});
            $("#pool-id").select2({width: '200px'});
        }
        else {
            $("#zone-id").select2({width: '415px'});
        }
        $("div#zone_select").show();
    },

    disableZones: function() {
        $("div#zone_select select").attr("disabled", true);
    },

    hideZones: function() {
        $("div#zone_select").hide();

        if ($("div#pool_select").is(":visible")) {
            $("#pool-id").select2({width: '415px'});
        }
    },

    toggleZones: function() {
        if (LayoutManager.zoneActive()) {
            LayoutManager.enableZones();
            LayoutManager.showZones();
        }
        else {
            LayoutManager.hideZones();
            LayoutManager.disableZones();
        }
    },

    enableFilters: function() {
        $('#choose_filters').removeClass('filter_text_disabled').addClass('filter_text');
        $('.pure-checkbox-disabled').removeClass('pure-checkbox-disabled');
        $('.se_filter').attr("disabled", false);
    },

    disableFilters: function() {
        $('#choose_filters').removeClass('filter_text').addClass('filter_text_disabled');
        $('.pure-checkbox').addClass('pure-checkbox-disabled');
        $('.se_filter').attr("disabled", true);
    },

    toggleFilters: function() {
        if (! DataManager.vehicle || DataManager.vehicleMap[DataManager.vehicle]["sb"]) {
            LayoutManager.enableFilters();
        }
        else {
            LayoutManager.disableFilters();
        }
    },

    createDate: function(date) {
        // in IE + Safari, if we pass the date the api sends right
        // into a date object, it outputs NaN
        // http://biostall.com/javascript-new-date-returning-nan-in-ie-or-invalid-date-in-safari
        var dateArray = date.split('-'),
            i,
            len = dateArray.length - 1;
        for (i = 0; i <= len; i++) {
            dateArray[i] = parseInt(dateArray[i], 10);
        }

        return new Date(dateArray[0], dateArray[1], dateArray[2]);
    },

    formatDate: function(dateObj) {
        //returns (mm/dd/yyyy) string representation of a date object
        return dateObj.getMonth() + '/' + dateObj.getDate() + '/' + dateObj.getFullYear().toString().substring(2);
    },

    convertDate: function(oldDate) {
        if (!oldDate) return 'Unknown';
        var dateArray = oldDate.split('-');
        return dateArray[1] + '/' + dateArray[2]+ '/' + dateArray[0];
    },

    numberWithCommas: function(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },

    toTitleCase: function(str) {
        // from http://stackoverflow.com/questions/5097875/help-parsing-string-city-state-zip-with-javascript
        return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();}).replace('U.s.', 'U.S.');
    }
};
