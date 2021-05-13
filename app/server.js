const express = require('express');
const app = express();
const PORT = 3000;
const path = require('path');

app.use(express.static(path.join(__dirname,'build')));
// app.use(express.static(__dirname));

app.listen(PORT, () => {
    console.log(`Server is running at ${PORT}`);
})