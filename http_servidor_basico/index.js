const express = require('express');

const app = express();
app.use(express.static('public'));

app.get('/testing', (req,res) => {
    res.send(`Llamaste desde ${req.headers.host}`)
});
app.listen(3000, () => {
    console.log('server is running on port 3000');
})