const express = require("express")

const authController = require("../controllers/authController")

const router = express.Router()

router.post("/sighnUp", authController.sighnUp)
router.post("/login", authController.login)

module.exports = router