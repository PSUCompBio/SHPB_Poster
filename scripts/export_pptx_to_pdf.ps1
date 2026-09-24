param(
    [string]$PptxPath = "pptx\Kolsky_Poster.pptx",
    [string]$PdfPath = "pptx\Kolsky_Poster_PPTX.pdf"
)

$fullPptx = (Resolve-Path $PptxPath).Path
$fullPdf = [System.IO.Path]::GetFullPath($PdfPath)

Write-Host "Opening PowerPoint..."
$ppt = New-Object -ComObject PowerPoint.Application
try {
    # Open presentation: ReadOnly, Untitled, WithWindow
    $pres = $ppt.Presentations.Open($fullPptx, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
    Write-Host "Saving as PDF: $fullPdf"
    $pres.SaveAs($fullPdf, 32) # 32 = ppSaveAsPDF
    $pres.Close()
    Write-Host "Successfully exported PDF!"
}
catch {
    Write-Error $_
}
finally {
    $ppt.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}
