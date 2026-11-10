// Stampa in PDF (A4) una pagina HTML creata da md2html.py, con WebKit di macOS.
// Uso: osascript -l JavaScript .claude/scripts/html2pdf.js "/percorso/pagina.html" "/percorso/uscita.pdf"
// Aspetta che MathJax abbia scritto le formule (la pagina mette il titolo "PRONTO").
ObjC.import('Cocoa');
ObjC.import('WebKit');

function aspetta(secondi) {
  $.NSRunLoop.currentRunLoop.runUntilDate($.NSDate.dateWithTimeIntervalSinceNow(secondi));
}

function run(argv) {
  var html = argv[0], pdf = argv[1];
  // un PDF vecchio con lo stesso nome farebbe credere che la stampa sia gia' finita
  $.NSFileManager.defaultManager.removeItemAtPathError(pdf, null);
  $.NSApplication.sharedApplication;
  var conf = $.WKWebViewConfiguration.alloc.init;
  var vista = $.WKWebView.alloc.initWithFrameConfiguration($.NSMakeRect(0, 0, 800, 1100), conf);
  vista.loadFileURLAllowingReadAccessToURL($.NSURL.fileURLWithPath(html), $.NSURL.fileURLWithPath('/'));
  var t = 0;
  while (t < 120) {
    aspetta(0.5); t += 0.5;
    if (!vista.isLoading && vista.title.js === 'PRONTO') break;
  }
  if (vista.title.js !== 'PRONTO') return 'ERRORE: la pagina non ha finito di caricare (' + vista.title.js + ')';
  aspetta(1);

  var info = $.NSPrintInfo.sharedPrintInfo.copy;
  info.paperSize = $.NSMakeSize(595.28, 841.89);
  info.topMargin = 0; info.bottomMargin = 0; info.leftMargin = 0; info.rightMargin = 0;
  info.horizontalPagination = $.NSPrintingPaginationModeFit;
  info.verticalPagination = $.NSPrintingPaginationModeAutomatic;
  info.jobDisposition = $.NSPrintSaveJob;
  info.dictionary.setObjectForKey($.NSURL.fileURLWithPath(pdf), $.NSPrintJobSavingURL);

  var op = vista.printOperationWithPrintInfo(info);
  op.showsPrintPanel = false;
  op.showsProgressPanel = false;
  var finestra = $.NSWindow.alloc.initWithContentRectStyleMaskBackingDefer($.NSMakeRect(0, 0, 800, 1100), 0, $.NSBackingStoreBuffered, false);
  finestra.contentView = vista;
  op.view.frame = $.NSMakeRect(0, 0, 800, 1100);
  op.runOperationModalForWindowDelegateDidRunSelectorContextInfo(finestra, undefined, undefined, undefined);
  var t2 = 0;
  while (t2 < 60 && !$.NSFileManager.defaultManager.fileExistsAtPath(pdf)) { aspetta(0.5); t2 += 0.5; }
  aspetta(1);
  return $.NSFileManager.defaultManager.fileExistsAtPath(pdf) ? 'ok ' + pdf : 'ERRORE: PDF non creato';
}
