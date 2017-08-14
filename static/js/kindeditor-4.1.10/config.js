KindEditor.ready(function (K) {
    K.create('textarea[name=content]', {
        width: 1000,
        height: 400,
        uploadJson: '/admin/upload/kindeditor'
    });
});