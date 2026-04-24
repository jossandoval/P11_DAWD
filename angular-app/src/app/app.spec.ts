import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { App } from './app';
import { WebService } from './web.service';

describe('App', () => {
  let fixture: any;
  let app: App;
  let httpMock: HttpTestingController;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App, HttpClientTestingModule],
      providers: [WebService]
    }).compileComponents();

    fixture = TestBed.createComponent(App);
    app = fixture.componentInstance;
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should create the app', () => {
    expect(app).toBeTruthy();
  });

  it('should set status online when web service responds successfully', () => {
    app.checkConnection();

    const req = httpMock.expectOne('https://jsonplaceholder.typicode.com/posts/1');
    expect(req.request.method).toBe('GET');
    req.flush({ id: 1, title: 'Test Post' });

    expect(app.status()).toBe('online');
  });

  it('should set status offline when web service returns an error', () => {
    app.checkConnection();

    const req = httpMock.expectOne('https://jsonplaceholder.typicode.com/posts/1');
    req.error(new ErrorEvent('Network error'));

    expect(app.status()).toBe('offline');
  });
});
