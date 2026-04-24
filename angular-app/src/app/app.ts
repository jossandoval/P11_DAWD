import { Component, signal } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { WebService } from './web.service';

@Component({
  selector: 'app-root',
  imports: [HttpClientModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('angular-app');
  readonly status = signal<'unknown' | 'online' | 'offline'>('unknown');

  constructor(private readonly webService: WebService) {}

  checkConnection(): void {
    this.webService.testConnection().subscribe((isConnected) => {
      this.status.set(isConnected ? 'online' : 'offline');
    });
  }
}
