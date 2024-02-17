const Post = require("../modules/postModel")

exports.getAllPosts = async (req, res, next) => {
    try {
        const posts = await Post.find()

        res.status(2)
    }   catch (e) {}
};