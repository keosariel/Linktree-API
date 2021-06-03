# Linktree-API
A simple implementation of the Linktree-API

This api is not fully functional as features would be added with respect to time and however all current functionalities might have bugs and I'll try my best to debug, as the api would be tested.

#### URI and Versioning
We hope to improve the API over time. The changes won't always be backward compatible, so we're going to use versioning. This first iteration will have URIs prefixed with https://`url`/v0/ and is structured as described below. There is currently no rate limit.

#### Error Codes

Code| Description | Misc
------------ | ------------ | ------------- 
**`E000`** | Bad Request |
**`E001`** | Insufficient Parameters,
**`E002`** | An error occured, Make sure all fields are input correctly
**`E004`** | Login or Signup
**`E005`** | SignUp Error
**`E006`** | Email or Password is incorrent
**`E007`** | User Cannot Edit Profile
**`E008`** | User Cannot Delete Profile
**`E009`** | User Does Not Exist
**`E010`** | User Cannot Edit Link
**`E011`** | User Cannot Delete Link
**`E012`** | Link Does Not Exist
**`E013`** | Exceeded Maximum Number Of Uploads
**`E014`** | Image Not Found
**`E015`** | Username Already Exists
**`E016`** | Email Already Exists
**`E017`** | Incorrect Password
**`E018`** | Email Doesn't Exists
**`E019`** | Expired Token (Request another one)

#### Regular Expressions

NAME| REGEX| Misc
------------ | ------------ | ------------- 
**`USERNAME`** | ^[a-z0-9_-]{3,15}$ |
**`EMAIL`** | [^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+ |
**`PASSWORD`** | ^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$ |

#### Accepted Media Formats

MIME TYPE | EXTENSION| Misc
------------ | ------------ | ------------- 
**`image/jpeg`** | .jpg | 
**`image/gif`** | .gif |
**`image/png`** | .png |

#### General Response Format

KEY| TYPE| Misc
------------ | ------------ | ------------- 
**`status_code`** | Int|
**`data`** | JSON Objest| 
**`error_code`** | String|
**`has_error`** | Boolean|
**`description`** | String|
**`error_data`** | JSON Object|


**Note:** Documentation comming soon
