using System.Diagnostics;
using System;

namespace ChessEngine
{
    internal static class Program
    {
        public static void Main()
        {
            string pythonInterpreterPath = @"C:\Users\91914\Desktop\Chess-engine-using-python\venv\Scripts\python.exe";
            string pythonScriptPath = @"C:\Users\91914\Desktop\Chess-engine-using-python\game.py";
            var process = new Process {
                StartInfo = new ProcessStartInfo {
                    FileName = pythonInterpreterPath,
                    Arguments = pythonScriptPath,
                    UseShellExecute = false
                }
            };
            process.Start();
            process.WaitForExit();
        }
    }
}