# Image Errors
ERROR_BAD_TYPE = "It appears this message's attachment(s) are not either JPEGs or PNGs"
ERROR_NO_IMAGE = "I'm sorry, I don't see any images in this message"
ERROR_INVALID_IMAGE = "It appears none of the images attached in this message are valid Pithka's screenshots. " \
                      "A valid screenshot will show the entirety of the 'Trials' tab"
ERROR_NO_LINKED_CLRS = "It appears no roles have been linked to clears yet. Use **/link** to link some!" \
                       "Use **/help** for instructions on how to do this"                 
ERROR_NO_RESULT = "No result file was generated. This likely means the image failed to crop properly"                
ERROR_NO_NEW_ROLES = "It appears there are no new roles to assign "           
           
                      
# Embed Strings
EMBED_ASSIGNED_TITLE = "Assigned Role(s)"
EMBED_ASSIGNED_DESC_1 = "Role Bot succesfully assigned the following "
EMBED_ASSIGNED_DESC_2 = " role(s) to "
EMBED_FOOTER_STR = "Created by alekwithk#5214 | www.esoresources.com"

EMBED_ERROR_TITLE = "An Error has Occured:"
EMBED_ERROR_HELP = "Use **/help** for more information on how this bot works"

EMBED_HELP_TITLE_EMOJI = "'Emoji' Command Instructions"
EMBED_HELP_TITLE_LINK = "'Link' Command Instructions"
EMBED_HELP_TITLE_IMG = "Image Information"

EMBED_INFO_TITLE = "Server Information"
EMBED_INFO_NO_EMOJI = "There is currently no emoji set for this server. "\
                      "The default is set to :white_check_mark: or you can use **/emoji** to set a new one!"
EMBED_INFO_EMOJI = "This server's emoji is currently set to: "
EMBED_INFO_NO_LINKS = "There are currently no linked roles in this server. Use **/link** to link a role!"
EMBED_INFO_LINKS = "The following is a list of all the roles that have been linked in this server: \n"

EMBED_ABOUT_TITLE = "About ESO Role Bot"

# CMND Strings
CMND_EMOJI_DESC = "If using a custom emoji, use the name NOT the actual emoji (i.e. 'sus' NOT ':sus:')"
CMND_EMOJI_TIP = "The emoji you'd like to use"

CMND_LINK_DESC = "Link the bot's supported clears to roles in your server"
CMND_LINK_BOT_TIP = "The shorthand code the bot uses to identify each clear"
CMND_LINK_ROLE_TIP = "The role in your server that you'd like to link to this clear"

CMND_HELP_DESC = "Help with the commands and functionalities of this bot"
CMND_HELP_TIP = "Select the topic you need help with"

HELP_VET_CLRS = "vdsr, vrg, vka, vss, vcr, vas, vhof, vmol, vso, vaa, vhrc"
HELP_PART_HM = "vdsr_twins, vdsr_reef, vrg_oax, vrg_bahsei, vka_yandir, vka_vrol, vss_ice, vss_fire, vas_llothis, vas_felms, vcr_1, vcr_2"
HELP_FULL_HM = "vdsr_hm, vrg_hm, vka_hm, vss_hm, vas_hm, vcr_hm, vhof_hm, vmol_hm, vso_hm, vaa_hm, vhrc_hm"
HELP_TRI = "vdsr_tri, vrg_tri, vka_tri, vss_tri, vcr_tri, vas_tri, vhof_tri"
HELP_EX = "vdsr_ex, vrg_ex, vka_ex, vss_ex, vcr_ex, vas_ex, vhof_ex, vmol_ex"
HELP_STUCK = "If you're still having issues feel free to contact the creator via Discord, listed below!"

CMND_ABOUT_DESC = "General information about what ESO Role Bot does and how it does it"

CMND_INFO_DESC = "Show your server's currently set emoji and linked roles"

# Permission Errors
CMND_PERM_DENIED = "ERROR: You must have server administrator permissions to run this command"

# Longform Strings
HELP_EMOJI = "The **/emoji** command is used to set the emoji an officer can use to react to a Pithka screenshot " \
             "and trigger a response from this bot. By default, it's set to :white_check_mark:\n\n" \
             "If using a default unicode emoji you can input the entire emoji into the emoji field. " \
             "However, if you're using a custom emoji, put only the emoji's name, not the actual emoji.\n\n" \
             "**For example:** \n" \
             "Default Emoji: :thumbsup:\n" \
             "Custom Emoji: thumbsup\n\n" \
             "If you're still having issues feel free to contact the creator via Discord, listed below!"
             
HELP_LINK = "The **/link** command is used to link the clears that the bot can validate with specific roles in your server. " \
            "The 'bot' field represents the tags the bot uses (listed below) and the 'role' field correspons to a role in the server. " \
            "You can either input the exact name of the role (e.g. 'Godslayer'), or you can use the role itself (e.g. '@Godslayer'). \n\n" \
            "So, for example, if you want to link your Godslayer role with the bot, you'd run the command **/link vss_tri Godslayer** \n\n" \
            "The following is a list of tags that the bot can recognize: "
            
ABOUT_INFO = "ESO Role Bot's goal is to remove some of the tedium that comes with reading Pithka Achievement Tracker screenshots " \
             "and manually assigning a Discord role for each clear. This bot uses computer vision via OpenCV to identify the classic " \
             "green checkmark and it's relative location on an image. The image has also been cropped using CV so that all images are " \
             "standardized. It can then relate these checkmark positions to known X, Y ratios from the top and left of the image " \
             "and assign corresponding Discord roles based on them. For example, if a check mark is found ~25\% off the left edge " \
             "and ~83\% off the top edge, the bot can be confident that that mark represents a vDSR clear. \n\n" \
             "Click the link at the top to visit **esoresources.com**, a great source for end game information! \n\n" \
             "If you need help with setting up or using the bot run the **/help** command, or contact the creator via the Discord shown below."
             
HELP_IMG = "Clicking the link title above will show you an example of a valid Pithka screenshot useable by this bot. " \
           "If the bot is failing to recognize an image, or assign roles, it could be for multiple reasons. \n\n" \
           "1. The image attachment is not a valid .JPG, .JPEG, or .PNG file image\n" \
           "2. The image is poor quality, either poorly cropped, or not a screenshot but rather a photo of a screen\n" \
           "3. The image is too messy or too obscured by addons/other visuals blocking parts of the image\n\n" \
           "In any of these cases, it's likely you'll have to manually assign roles, as due to the nature of computer vision " \
           "and the vast array of possible images someone could submit, it's not possible to account for all errors."            