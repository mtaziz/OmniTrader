Ext.application({
    name: 'Sencha',

    launch: function () {
        var panel = Ext.create('OmniTrader.view.TagSearchView')
        Ext.Viewport.add(panel);
    }
});