#!/usr/bin/env python3
import pandas

standard_notes = ['C', 'C#', 'D', 'D#', 'E',
                  'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

tonic_notes = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

standard_to_tonic = {
    'C': 'do',
    'D': 're',
    'E': 'mi',
    'F': 'fa',
    'G': 'sol',
    'A': 'la',
    'B': 'si',
}

standard_A_frequency = 440.0

standard_A_index = standard_notes.index('A')

standard_table = {k: [] for k in standard_notes}

tonic_table = {k: [] for k in tonic_notes}

for i in range(0 - 2 * len(standard_notes), 3 * len(standard_notes)):
    note_index = (i + 2 * len(standard_notes)) % len(standard_notes)
    note = standard_notes[note_index]
    frequency = standard_A_frequency * (2 ** ((i-standard_A_index) / 12))
    standard_table[note].append(frequency)
    if note in standard_to_tonic:
        tonic_note = standard_to_tonic[note]
        tonic_table[tonic_note].append(frequency)

dataframe = pandas.DataFrame(data=standard_table)
dataframe.to_csv('standard_frequency.csv', index=False)

dataframe = pandas.DataFrame(data=tonic_table)
dataframe.to_csv('tonic_frequency.csv', index=False)
