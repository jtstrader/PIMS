import { Component, OnInit } from '@angular/core';
import { Subscriber, Subscription } from 'rxjs';
import { IDeathRatesByState } from '../interfaces/ideath-rates-by-state';
import { DeathRatesByStateService } from '../services/death-rates-by-state.service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  constructor(private deathRatesByState: DeathRatesByStateService) { }

  sub!: Subscription;
  deathRates!: IDeathRatesByState[];
  errorMessage: string = "";

  backId: number = 0;
  bckgrdColors: string[] = ["#fff", "#ccc"];

  ngOnInit(): void {
    this.sub = this.deathRatesByState.getDeathRates().subscribe({
      next: drs => this.deathRates = drs,
      error: err => this.errorMessage = err
    });
  }

  alternateBackgroundColor(): string {
    return this.bckgrdColors[this.backId == 0 ? this.backId++ : this.backId--]
  }

  // return a string to include trailing zeros
  deathRateAdjust(death_rate: number): string {
    return (death_rate * 100).toFixed(2);
  }

}
