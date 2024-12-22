
@set TARGET_DIR=%1
@if exist %TARGET_DIR% (
    echo Directory %TARGET_DIR% exists.
) else (
    @xcopy /E/Y/I "template" %TARGET_DIR%
)

@cd %TARGET_DIR%
@code .
