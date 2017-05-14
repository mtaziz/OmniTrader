Ext.define('Stock', {
    extend: 'Ext.data.Model',

    config: {
        fields: ['id', 'ticker', 'name','tags']
    }
});