const User = require("../modules/userModel");
const bcrypt = require("bcryptjs")

exports.sighnUp = async (req, res) => {
    const {username, password} = req.body;

    try {
        const hashpassowrd = await bcrypt.hash(password, 12);
        const newUser = await User.create ({
            username,
            password: hashpassowrd,
        });
        res.status(201).json({
            status: "success",
            data: {
                user: newUser
            },
        });
    } catch (e) {
        res.status(400).json({
            status: "fail",
        });
    }
};

exports.login = async (req, res) => {
    const {username, password} = req.body;
    try {
        const user = await User.findOne({username})
        if (!user) {
            return res.status(404).json({
                status: "fail",
                message: "user not found"
            });
        };
        const isCorrect = await bcrypt.compare(password, user.password)

        if (isCorrect) {
            res.status(200).json({
                status: "success"
            });
        }   else {
            res.status(400).json({
                status: "success",
                data: {
                    user: newUser,
                },
            });
        }
    } catch (e) {
        res.status(400).json({
            status: "fail",

        });
    }
}