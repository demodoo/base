odoo.define('field_time.time', function (require) {
"use strict";

    var field_registry = require('web.field_registry');
    var Field = field_registry.get('datetime');

    var FieldTime = Field.extend({

        _renderReadonly: function () {
            var show_value = this._formatValue(this.value);
            var show_time = show_value.split(' ');
            this.$el.text(show_time[1]);
        },

    });

    field_registry.add('time', FieldTime);

    return {
        FieldTime: FieldTime
    };

});
