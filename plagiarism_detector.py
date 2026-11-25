"""
Source Code Plagiarism Detection Using Token Streams
=====================================================

A beginner-friendly Python desktop application built with Tkinter.
It lets the user select two .py files, extracts their token streams
(ignoring comments and unnecessary whitespace), compares the sequences,
and reports a similarity percentage with a High / Moderate / Low rating.

Standard library only: tkinter, tokenize, io, difflib.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tokenize
import io
import difflib


class PlagiarismDetectorApp:
    """Main application class for the plagiarism detector GUI."""

    def __init__(self, root):
        self.root = root
        self.root.title("Source Code Plagiarism Detector")
        self.root.geometry("750x560")
        self.root.resizable(True, True)

        # Variables to hold the selected file paths
        self.file1_path = tk.StringVar()
        self.file2_path = tk.StringVar()

        # Build the user interface
        self.setup_ui()

    def setup_ui(self):
        """Create and arrange all widgets."""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Make the window expand nicely
        self.root.columnconfigure(0, weight=1)
        # ---------- Result panel ----------
        result_frame = ttk.LabelFrame(main_frame, text="Comparison Result", padding="15")
        result_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        result_frame.columnconfigure(1, weight=1)

        ttk.Label(result_frame, text="Similarity:").grid(
            row=0, column=0, sticky=tk.W
        )
        self.similarity_label = ttk.Label(
            result_frame, text="-- %", font=("Segoe UI", 14, "bold")
        )
        self.similarity_label.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))

        ttk.Label(result_frame, text="Category:").grid(
            row=1, column=0, sticky=tk.W, pady=(8, 0)
        )
        self.category_label = ttk.Label(
            result_frame, text="--", font=("Segoe UI", 12, "bold")
        )
        self.category_label.grid(row=1, column=1, sticky=tk.W, padx=(10, 0), pady=(8, 0))

        # ---------- Details text area ----------
        ttk.Label(main_frame, text="Details:").grid(
            row=5, column=0, sticky=tk.W, pady=(18, 5)
        )
        self.details_text = tk.Text(main_frame, height=11, width=80, wrap=tk.WORD)
        self.details_text.grid(
            row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10)
        )

        # Scrollbar for the details area
        scrollbar = ttk.Scrollbar(
            main_frame, orient=tk.VERTICAL, command=self.details_text.yview
        )
        scrollbar.grid(row=6, column=3, sticky=(tk.N, tk.S))
        self.details_text.configure(yscrollcommand=scrollbar.set)

        # ---------- Status bar ----------
        self.status_var = tk.StringVar(
            value="Ready - select two Python files to compare"
        )
        status_bar = ttk.Label(
            main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W
        )
        status_bar.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # ---------- Title ----------
        title_label = ttk.Label(
            main_frame,
            text="Source Code Plagiarism Detector",
            font=("Segoe UI", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # ---------- File 1 ----------
        ttk.Label(main_frame, text="First Python File:").grid(
            row=1, column=0, sticky=tk.W, pady=6
        )
        self.file1_entry = ttk.Entry(main_frame, textvariable=self.file1_path, width=55)
        self.file1_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 5), pady=6)
        ttk.Button(main_frame, text="Browse...", command=self.browse_file1).grid(
            row=1, column=2, pady=6
        )

        # ---------- File 2 ----------
        ttk.Label(main_frame, text="Second Python File:").grid(
            row=2, column=0, sticky=tk.W, pady=6
        )
        self.file2_entry = ttk.Entry(main_frame, textvariable=self.file2_path, width=55)
        self.file2_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(10, 5), pady=6)
        ttk.Button(main_frame, text="Browse...", command=self.browse_file2).grid(
            row=2, column=2, pady=6
        )

        # ---------- Compare button ----------
        self.compare_btn = ttk.Button(
            main_frame, text="Compare Files", command=self.compare_files
        )
        self.compare_btn.grid(row=3, column=0, columnspan=3, pady=18)
