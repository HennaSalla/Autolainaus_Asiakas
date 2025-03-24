# NSIS INSTALLER TEMPLATE WITH MODERN UI
# =======================================================

# Include Modern UI
  # Let's use modern look importing header file
  !include "MUI2.nsh"

# --- Include end

# General

  # Name and installer file name, do not use plain setup.exe as OutFile
  Name "Autolainaus"
  OutFile "autolainausInstaller.exe"
  Unicode True

  # Default installation folder: user's application data directory
  InstallDir "$PROGRAMFILES\Autolainausasiakas"
  
  # Get installation folder from registry if available (reinstall)
  InstallDirRegKey HKCU "Software\Autolainausasiakas" ""

  # Request application privileges for Windows Vista or later: user | admin
  RequestExecutionLevel admin

# --- General end

# Variable declarations

  Var StartMenuFolder

# --- Variable definitions end

# Interface Settings

  # Set icon for installer window
  !define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\orange-install.ico"

  # Add a bitmap (150 x 57 px) for a logo into the header of the installer page
  !define MUI_HEADERIMAGE
  !define MUI_HEADERIMAGE_BITMAP "VWbg.bmp"

  # Set left side image for start and end page
  !define MUI_WELCOMEFINISHPAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Wizard\orange.bmp"

  # Check if user really wants to abort
  !define MUI_ABORTWARNING

  # Show all languages, despite user's codepage
  !define MUI_LANGDLL_ALLLANGUAGES

# --- end Interface settings

# Language Selection Dialog Settings

  # Remember the installer language -> language not asked when installer restarted
  !define MUI_LANGDLL_REGISTRY_ROOT "HKCU" 
  !define MUI_LANGDLL_REGISTRY_KEY "Software\Autolainausasiakas" 
  !define MUI_LANGDLL_REGISTRY_VALUENAME "Installer Language"

# --- Language Selection Dialog Settings end

# Pages
  !insertmacro MUI_PAGE_WELCOME

  # License file containing the GNU GPL 3 information
  !insertmacro MUI_PAGE_LICENSE "LICENSE"

  !insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  
  # Start Menu Folder Page Configuration
  !define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKCU" 
  !define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\Autolainausasiakas" 
  !define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"
  
  !insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder
  
  !insertmacro MUI_PAGE_INSTFILES
  
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES

# --- Pages end

# Languages, 1st is the default
 
  !insertmacro MUI_LANGUAGE "Finnish"
  !insertmacro MUI_LANGUAGE "English"

# --- Languages end

# Installer Sections

# Section for choosing the program 
Section "Autolainaussovellus asiakas" SecProgram

  SetOutPath "$INSTDIR"
  
  # Files to put into the installation directory from the distribution folder
  File /r "dist\user\"

  # Store installation folder to registry
  WriteRegStr HKCU "Software\Autolainausasiakas" "" $INSTDIR
  
  # Create uninstaller
  WriteUninstaller "$INSTDIR\UninstallAutolainausasiakas.exe"
  
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
    
    # Create shortcuts
    CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
    CreateShortcut "$SMPROGRAMS\$StartMenuFolder\Autolainausasiakas.lnk" "$INSTDIR\user.exe"
    CreateShortcut "$SMPROGRAMS\$StartMenuFolder\UninstallAutolainausasiakas.lnk" "$INSTDIR\UninstallAutolainausasiakas.exe"
  
  !insertmacro MUI_STARTMENU_WRITE_END

SectionEnd

# Section for optional files or directories
# Section "NameOfFile" secAdditions
#     SetOutPath "$INSTDIR\AdditionsFolderName"
  
# Dictionary files to put into Additional subdirectory
#   File "*.something"
#   File "*.otherType"
# SectionEnd

# --- # Installer Sections end

# Installer Functions

# A function for asking the installation language at startup
Function .onInit
  
  !insertmacro MUI_LANGDLL_DISPLAY

FunctionEnd

# --- Installer Functions


# Descriptions

  # Language strings
  LangString DESC_SecProgram ${LANG_FINNISH} "Autojen lainaus- ja palautussovellus"
  LangString DESC_SecProgram ${LANG_ENGLISH} "A program to lend and return vehicles"
  # LangString DESC_secAdditions ${LANG_FINNISH} "Additional content explaned in finnish"
  # LangString DESC_secAdditions ${LANG_ENGLISH} "Additional content explaned in english"

  # Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecProgram} $(DESC_SecProgram)
    # !insertmacro MUI_DESCRIPTION_TEXT ${secAdditions} $(DESC_secAdditions)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END
 
# --- Descriptions end

# Uninstaller Section
Section "Uninstall"

  # Remove files and folders from installation directory, if not successfull remove after reboot
  RMDir /r /REBOOTOK $INSTDIR
  
  !insertmacro MUI_STARTMENU_GETFOLDER Application $StartMenuFolder

  # Remove start menu items  
  Delete "$SMPROGRAMS\$StartMenuFolder\Autolainausasiakas.lnk"
  Delete "$SMPROGRAMS\$StartMenuFolder\UninstallAutolainaus.lnk"
  RMDir "$SMPROGRAMS\$StartMenuFolder"
  
  # Clean the registry by removing all keys under NameOfApp
  
  DeleteRegKey HKCU "Software\Autolainausasiakas"

SectionEnd

#--- Uninstaller Section end

# A function for the uninstaller's language
Function un.onInit

  !insertmacro MUI_UNGETLANGUAGE
  
FunctionEnd

# --- Unistaller language function end