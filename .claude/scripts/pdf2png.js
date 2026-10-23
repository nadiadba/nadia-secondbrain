// Converte le pagine di un PDF in immagini PNG, con gli strumenti gia' presenti nel Mac (PDFKit).
// Uso: osascript -l JavaScript .claude/scripts/pdf2png.js FILE.pdf CARTELLA_USCITA [prima] [ultima] [larghezza]
ObjC.import("PDFKit"); ObjC.import("AppKit");
function run(a) {
  var doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(a[0]));
  if (!doc || doc.isNil()) return "PDF non leggibile: " + a[0];
  var out = a[1]; $.NSFileManager.defaultManager.createDirectoryAtPathWithIntermediateDirectoriesAttributesError(out, true, $(), $());
  var n = doc.pageCount, da = a[2] ? parseInt(a[2]) : 1, a_ = a[3] ? Math.min(parseInt(a[3]), n) : n, w = a[4] ? parseInt(a[4]) : 1400;
  for (var i = da; i <= a_; i++) {
    var p = doc.pageAtIndex(i - 1), r = p.boundsForBox($.kPDFDisplayBoxMediaBox);
    var h = Math.round(w * r.size.height / r.size.width);
    var img = p.thumbnailOfSizeForBox($.NSMakeSize(w, h), $.kPDFDisplayBoxMediaBox);
    var rep = $.NSBitmapImageRep.imageRepWithData(img.TIFFRepresentation);
    var png = rep.representationUsingTypeProperties($.NSBitmapImageFileTypePNG, $());
    png.writeToFileAtomically(out + "/pagina-" + ("00" + i).slice(-3) + ".png", true);
  }
  return "pagine " + da + "-" + a_ + " di " + n + " salvate in " + out;
}
