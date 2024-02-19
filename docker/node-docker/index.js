const express = require("express");
// const { connect } = require("http2");
const { default: mongoose } = require("mongoose");
const {
    MONGO_USER, 
    MONGO_PASSWORD, 
    MONGO_IP, 
    MONGO_PORT
} = require("./config/config")


const postRouter = require("./routes/postRoutes")
const userRouter = require("./routes/userRoutes")

const app = express();

const mongoURL = `mongodb://${MONGO_USER}:${MONGO_PASSWORD}@${MONGO_IP}:${MONGO_PORT}/?authSource=admin`

const connectWithRetry = () => {
    mongoose
.connect(mongoURL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    // useFindAndModify: false
})
.then(() => console.log("succesful conected to DB"))
.catch((e) => {
    console.log(e)
    setTimeout(connectWithRetry, 5000)
});
}

connectWithRetry();

app.use(express.json());

app.get("/", (req, res) => {
    res.send("<h2>Hello everyone')</h2>")
});

app.use("/api/v1/posts", postRouter);
app.use("/api/v1/users", userRouter);
const port = process.env.PORT || 3000;

app.listen(port, () => console.log(`listening on port ${port}`));