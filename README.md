
# Telegram Bot for Game




## Appendix

This is the telegram bot for Game use. The bot will record multiple user input and output the result by list. User can input and remove the record from List. There some admin instructions to display more information.


## Version Control



### Version 1.0.0
* Created a bot to display the output list
### Version 1.1.0
* Add the input successful message
* Generate the result list line by line
* Display Error message
* Add the admin instruction to display extra information
### Version 2.0.0
* Add the admin instruction to remove record
* Handle duplicate input
* Enhance the remove function 
### Version 3.0.0
* Open the admin control to selected user
## User Guide

### Installation

```http
  Telgram Bot Name: @NajaiReg_bot
```

#### Normal User


| Command     | Description                |
| :-------- | :------------------------- |
| `/join [name]`  | Input the [name] to list |
| `/delete [name]`  | Remove the [name] to list; Only creator can remove the record |
| `/show`  | Display the output list |
| `/close`  | Terminte the bot |
| `/help`  | Call the user manual |


#### Admin User
| Command     | Description                |
| :-------- | :------------------------- |
| `/start`  | Initial the bot |
| `/sushow`  | Display the result list with the record inputer |
| `/sudelete [name]`  | Remove the [name] to list; |


