var my_store = Ext.create("Ext.data.Store", {
    model: "Stock",
    proxy: {
        type: "ajax",
        url: root_url + "/stocks/tags/",
        extraParams: {
            tags: '雄安',
            format: 'json'
        },
        reader: {
            type: "json"
        }
    },
    autoLoad: true
});

var thestore = Ext.create('Ext.data.Store', {
    model: "Stock",
    autoLoad: true,
    data: [{id: 1, name: 'zxzq', ticker: '600030'}]
});
Ext.define('OmniTrader.view.TagSearchView', {
    extend: 'Ext.Panel',
    alias: ['ot-tagsearchview'],

    config: {
        layout: 'hbox',
        items: [
            {
                xtype: 'textfield',
                itemId: 'tagSearchField',
                docked: 'top',
                placeHolder: 'Enter tags',
                enableKeyEvents: true,
                listeners: {
                    'action': function (field, event, options) {
                        my_store.load({params: {tags: field.getValue()}})
                    }
                }
            }, {
                xtype: 'list',
                store: my_store,
                itemTpl: '{ticker} {name}',
                listeners: {
                    'itemtap': function (list, index, target, record, e, eOpts) {
                        var detailview = Ext.create('ot-stockdetailview');
                        detailview.viewStock(record.data)
                        //TODO: Change hard binding to use controller.
                        this.up().up().push(detailview)
                    }
                },
                flex: 1
            }
        ]

    }
});