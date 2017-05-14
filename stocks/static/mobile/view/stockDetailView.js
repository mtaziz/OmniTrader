Ext.define('OmniTrader.view.StockDetailView', {
    extend: 'Ext.Panel',
    alias: ['ot-stockdetailview'],

    config: {
        height: 'auto',
        layout:'vbox',
        defaults:{
            xtype:'label',
            margin:'5',
        },
        items: [
            {itemId: 'lbl_ticker'},
            {itemId: 'lbl_name'},
            {itemId: 'lbl_tags'}
        ]
    },
    viewStock: function (stock) {
        this.getComponent('lbl_ticker').setHtml(stock.ticker);
        this.getComponent('lbl_name').setHtml(stock.name);
        this.getComponent('lbl_tags').setHtml(stock.tags);
    }
});